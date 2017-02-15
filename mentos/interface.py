from __future__ import absolute_import, division, print_function

import logging
import sys

log = logging.getLogger(__name__)


class Scheduler(object):

    def on_registered(self, driver, framework_id, master):# pragma: no cover
        """Event handler triggered when the scheduler successfully registers
           with a master.
        Parameters
        ----------
        driver: SchedulerDriver
            Interface for interacting with Mesos Master
        framework_id : string
            Unique ID generated by the master
        master : Master
            Information about the master itself
        Returns
        -------
        self
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_reregistered(self, driver, framework_id, master):# pragma: no cover
        """Event handler triggered when the scheduler re-registers with a newly
           elected master.
        This is only called when the scheduler has previously been registered.
        masterInfo contains information about the newly elected master.
        Parameters
        ----------
        driver: SchedulerDriver
            Interface for interacting with Mesos Master
        framework_id : string
            Unique ID generated by the master
        master : Master
            Information about the master itself
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_disconnected(self, driver):# pragma: no cover
        """Event handler triggereg when the scheduler becomes disconnected from
           the master.
        (e.g. the master fails and another is taking over)
        Parameters
        ----------
        driver: SchedulerDriver
            Interface for interacting with Mesos Master
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_offers(self, driver, offers):# pragma: no cover
        """Event handler triggered when resources have been offered to this
           framework.
        A single offer will only contain resources from a single slave.
        Resources associated with an offer will not be re-offered to _this_
        framework until either (a) this framework has rejected those resources
        (see SchedulerDriver.launchTasks) or (b) those resources have been
        rescinded (see Scheduler.on_rescinded).
        Note that resources may be concurrently offered to more than one
        framework at a time (depending on the allocator being used).  In that
        case, the first framework to launch tasks using those resources will be
        able to use them while the other frameworks will have those resources
        rescinded (or if a framework has already launched tasks with those
        resources then those tasks will fail with a TASK_LOST status and a
        message saying as much).
        Parameters
        ----------
        driver: SchedulerDriver
            Interface for interacting with Mesos Master
        offers: list of Offer
            Resource offer instances
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_rescinded(self, driver, offer_id):# pragma: no cover
        """Event handler triggered when an offer is no longer valid.
        (e.g., the slave was lost or another framework used resources in the
        offer)
        If for whatever reason an offer is never rescinded (e.g., dropped
        message, failing over framework, etc.), a framework that attempts to
        launch tasks using an invalid offer will receive TASK_LOST status
        updates for those tasks (see Scheduler.on_offers).
        Parameters
        ----------
        driver: SchedulerDriver
            Interface for interacting with Mesos Master
        offer_id: string
            The unique identifier of the Mesos offer
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_rescind_inverse(self, driver, offer_id):# pragma: no cover
        """Event handler triggered when an offer is no longer valid.
        (e.g., the slave was lost or another framework used resources in the
        offer)
        If for whatever reason an offer is never rescinded (e.g., dropped
        message, failing over framework, etc.), a framework that attempts to
        launch tasks using an invalid offer will receive TASK_LOST status
        updates for those tasks (see Scheduler.on_offers).
        Parameters
        ----------
        driver: SchedulerDriver
            Interface for interacting with Mesos Master
        offer_id: string
            The unique identifier of the Mesos offer
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_update(self, driver, status):# pragma: no cover
        """Event handler triggered when the status of a task has changed.
        (e.g., a slave is lost and so the task is lost, a task finishes and an
        executor sends a status update saying so, etc.)
        If implicit acknowledgements are being used, then returning from this
        callback _acknowledges_ receipt of this status update!
        If for  whatever reason the scheduler aborts during this callback (or
        the process exits) another status update will be delivered (note,
        however, that this is currently not true if the slave sending the status
        update is lost/fails during that time).
        If explicit acknowledgements are in use, the scheduler must acknowledge
        this status on the driver.
        Parameters
        ----------
        driver: SchedulerDriver
            Interface for interacting with Mesos Master
        status: string
            Task Status
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_message(self, driver, executor_id, slave_id, message):# pragma: no cover
        """Event handler triggered when an executor sends a message.
        These messages are best effort; do not expect a framework message to be
        retransmitted in any reliable fashion.
        Parameters
        ----------
        driver: SchedulerDriver
            Interface for interacting with Mesos Master
        executor_id: string
            The unique identifier of the Mesos executor the message came from
        slave_id: string
            The unique identifier of the Mesos slave the message came from
        message: string
            Arbitrary byte stream
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_slave_lost(self, driver, slave_id):# pragma: no cover
        """Event handler triggered when a slave has been determined unreachable.
        (e.g., machine failure, network partition.)
        Most frameworks will need to reschedule any tasks launched on this slave
        on a new slave.
        Parameters
        ----------
        driver: SchedulerDriver
            Interface for interacting with Mesos Master
        slave_id: string
            The unique identifier of the lost Mesos slave
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_executor_lost(self, driver, executor_id, slave_id, status):# pragma: no cover
        """Event handler triggered when an executor has exited/terminated.
        Note that any tasks running will have TASK_LOST status updates
        automatically generated.
        NOTE: This callback is not reliably delivered.
        Parameters
        ----------
        driver: SchedulerDriver
            Interface for interacting with Mesos Master
        executor_id: string
            The unique identifier of the lost Mesos executor
        slave_id: string
            The unique identifier of the Mesos slave where the executor loss
            happened
        status: int
            TODO: figure it out
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_error(self, driver, message):# pragma: no cover
        """Event handler triggered when there is an unrecoverable error in the
           scheduler or scheduler driver.
        The driver will be aborted BEFORE invoking this callback.
        Parameters
        ----------
        driver: SchedulerDriver
            Interface for interacting with Mesos Master
        message: string
            Arbitrary byte stream
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_heartbeat(self, driver, message):# pragma: no cover
        """Event handler triggered when a heartbeat is recieved from the Master.
        Parameters
        ----------
        driver: ExecutorDriver
            Interface for interacting with Mesos Agent
        message: string
            Arbitrary byte stream
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_outbound_error(self, driver, request, endpoint, error):# pragma: no cover
        """Event handler triggered when an error has occured when sending data to the Master
        Parameters
        ----------
        driver: ExecutorDriver
            Interface for interacting with Mesos Agent
        request: dict
            Request sent to endpoint
        endpoint: str
            Endpoint
        error: Exception
            Raised exception
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_outbound_success(self, driver, request):# pragma: no cover
        """Event handler triggered when a request was successful when sending data to the Master
        Parameters
        ----------
        driver: ExecutorDriver
            Interface for interacting with Mesos Agent
        request: dict
            Request sent to endpoint
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))


class Executor(object):
    """Base class for Mesos executors.
    Users' executors should extend this class to get default implementations of
    methods they don't override.
    """

    def on_registered(self, driver, executor, framework, slave):# pragma: no cover
        """Event handler triggered when the executor driver has been able to
           successfully connect with Mesos.
        In particular, a scheduler can pass some data to its executors through
        the FrameworkInfo.ExecutorInfo's data field.
        Parameters
        ----------
        driver: ExecutorDriver
            Interface for interacting with Mesos Agent
        executor: Executor
            The unique identifier of the lost Mesos executor
        framework: Framework
            TODO: write docs
        slave: Salve
            TODO: write docs
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_reregistered(self, driver, slave):# pragma: no cover
        """Event handler triggered when the executor re-registers with a
           restarted slave.
        Parameters
        ----------
        driver: ExecutorDriver
            Interface for interacting with Mesos Agent
        slave: Slave
            TODO: write docs
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_disconnected(self, driver):# pragma: no cover
        """Event handler triggered when the executor becomes "disconnected" from
           the slave.
        (e.g., the slave is being restarted due to an upgrade)
        Parameters
        ----------
        driver: ExecutorDriver
            Interface for interacting with Mesos Agent
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_launch(self, driver, task):# pragma: no cover
        """Event handler triggered when a task has been launched on this
           executor (initiated via Scheduler.launch).
        Note that this task can be realized with a thread, a process, or some
        simple computation, however, no other callbacks will be invoked on this
        executor until this callback has returned.
        Parameters
        ----------
        driver: ExecutorDriver
            Interface for interacting with Mesos Agent
        task: Task
            TODO: write docs
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_kill(self, driver, task_id):# pragma: no cover
        """Event handler triggered when a task running within this executor has
           been killed (via SchedulerDriver.kill).
        Note that no status update will be sent on behalf of the executor, the
        executor is responsible for creating a new TaskStatus (i.e., with
        TASK_KILLED) and invoking ExecutorDriver's update method.
        Parameters
        ----------
        driver: ExecutorDriver
            Interface for interacting with Mesos Agent
        task_id: string
            Unique identifier of the killed task
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_message(self, driver, message):# pragma: no cover
        """Event handler triggered when a framework message has arrived for this
           executor.
        These messages are best effort; do not expect a framework message to be
        retransmitted in any reliable fashion.
        Parameters
        ----------
        driver: ExecutorDriver
            Interface for interacting with Mesos Agent
        message: string
            Arbitrary byte stream
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_shutdown(self, driver):# pragma: no cover
        """Event handler triggered when the executor should terminate all of its
           currently running tasks.
        Note that after Mesos has determined that an executor has terminated any
        tasks that the executor did not send terminal status updates for (e.g.,
        TASK_KILLED, TASK_FINISHED, TASK_FAILED, etc) a TASK_LOST status update
        will be created.
        Parameters
        ----------
        driver: ExecutorDriver
            Interface for interacting with Mesos Agent
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_error(self, driver, message):# pragma: no cover
        """Event handler triggered when a fatal error has occurred with the
           executor and/or executor driver.
        The driver will be aborted BEFORE invoking this callback.
        Parameters
        ----------
        driver: ExecutorDriver
            Interface for interacting with Mesos Agent
        message: string
            Arbitrary byte stream
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))


    def on_acknowledged(self,driver, task_id, uuid):  # pragma: no cover
        """Event handler triggered when a task update has successfully been acknowledged
        ----------
        driver: ExecutorDriver
            Interface for interacting with Mesos Agent
        task_id: string
            Mesos Task ID
        uuid: UUID
            Acknowledge UUID
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_outbound_error(self, driver, request, endpoint, error):  # pragma: no cover
        """Event handler triggered when an error has occured when sending data to the Executor
        Parameters
        ----------
        driver: ExecutorDriver
            Interface for interacting with Mesos Agent
        request: dict
            Request sent to endpoint
        endpoint: str
            Endpoint
        error: Exception
            Raised exception
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))

    def on_outbound_success(self, driver, request):# pragma: no cover
        """Event handler triggered when a request was successful when sending data to the Executor
        Parameters
        ----------
        driver: ExecutorDriver
            Interface for interacting with Mesos Agent
        request: dict
            Request sent to endpoint
        """
        log.debug("{function} not implemented".format(function=sys._getframe().f_code.co_name))
